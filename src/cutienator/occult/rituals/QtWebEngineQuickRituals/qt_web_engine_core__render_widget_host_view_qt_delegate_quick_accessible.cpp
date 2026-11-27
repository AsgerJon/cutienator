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

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 96, as _ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible7isValidEv
namespace QtWebEngineCore {
inline bool RenderWidgetHostViewQtDelegateQuickAccessible::isValid() const
{
    if (!viewAccessible() || !viewAccessible()->isValid())
        return false;

    return QAccessibleObject::isValid();
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 104, as _ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible6parentEv
namespace QtWebEngineCore {
inline QAccessibleInterface *RenderWidgetHostViewQtDelegateQuickAccessible::parent() const
{
    return viewAccessible()->parent();
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 109, as _ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible4textEN11QAccessible4TextE
namespace QtWebEngineCore {
inline QString RenderWidgetHostViewQtDelegateQuickAccessible::text(QAccessible::Text) const
{
    return QString();
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 114, as _ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible4roleEv
namespace QtWebEngineCore {
inline QAccessible::Role RenderWidgetHostViewQtDelegateQuickAccessible::role() const
{
    return QAccessible::Client;
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 119, as _ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible5stateEv
namespace QtWebEngineCore {
inline QAccessible::State RenderWidgetHostViewQtDelegateQuickAccessible::state() const
{
    return viewAccessible()->state();
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 124, as _ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible10focusChildEv
namespace QtWebEngineCore {
inline QAccessibleInterface *RenderWidgetHostViewQtDelegateQuickAccessible::focusChild() const
{
    return viewAccessible()->focusChild();
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 129, as _ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible10childCountEv
namespace QtWebEngineCore {
inline int RenderWidgetHostViewQtDelegateQuickAccessible::childCount() const
{
    return viewAccessible()->childCount();
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 134, as _ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible5childEi
namespace QtWebEngineCore {
inline QAccessibleInterface *RenderWidgetHostViewQtDelegateQuickAccessible::child(int index) const
{
    return viewAccessible()->child(index);
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginequick/qquickwebengine_accessible.cpp, line 139, as _ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible12indexOfChildEPK20QAccessibleInterface
namespace QtWebEngineCore {
inline int RenderWidgetHostViewQtDelegateQuickAccessible::indexOfChild(const QAccessibleInterface *c) const
{
    return viewAccessible()->indexOfChild(c);
}
}  // namespace QtWebEngineCore
//  -----------------------------------------------------------------------

//  bool
//      QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::isVal
//      id() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible7isValidEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible *self) {
  return self->isValid();
}

//  QAccessibleInterface
//      *QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::pare
//      nt() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible6parentEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible *self) {
  return self->parent();
}

//  QString QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::t
//      ext(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible4textEN11QAccessible4TextE(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  QAccessible::Role
//      QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::role(
//      ) const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible4roleEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible *self) {
  return self->role();
}

//  QAccessible::State
//      QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::state
//      () const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible5stateEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible *self) {
  return new QAccessible::State(self->state());
}

//  QAccessibleInterface *QtWebEngineCore::RenderWidgetHostViewQtDelegateQuic
//      kAccessible::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible10focusChildEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible *self) {
  return self->focusChild();
}

//  int QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::child
//      Count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible10childCountEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible *self) {
  return self->childCount();
}

//  QAccessibleInterface *QtWebEngineCore::RenderWidgetHostViewQtDelegateQuic
//      kAccessible::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible5childEi(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible *self,
    int index) {
  return self->child(index);
}

//  int QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::index
//      OfChild(const QAccessibleInterface *a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible12indexOfChildEPK20QAccessibleInterface(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible *self,
    const QAccessibleInterface *a0) {
  return self->indexOfChild(a0);
}

//  QString QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::t
//      ext(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible4textEN11QAccessible4TextE(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible *self,
    QAccessible::Text t) {
  return new QString(
      self->QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::text(
          t));
}

//  QAccessible::Role
//      QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::role(
//      ) const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK15QtWebEngineCore45RenderWidgetHostViewQtDelegateQuickAccessible4roleEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible *self) {
  return self->QtWebEngineCore::RenderWidgetHostViewQtDelegateQuickAccessible::role();
}

#endif  // QT_CONFIG(accessibility)
