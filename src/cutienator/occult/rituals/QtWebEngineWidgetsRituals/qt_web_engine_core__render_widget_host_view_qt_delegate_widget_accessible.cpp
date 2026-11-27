//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineWid
//  gets/6.12.0/QtWebEngineWidgets/private/qwebengine_accessible_p.h, Qt
//  6.12.0. Changes made here are lost.
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

//  from ../qtwebengine/src/webenginewidgets/qwebengine_accessible.cpp, line 70, as _ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible7isValidEv
namespace QtWebEngineCore {
inline bool RenderWidgetHostViewQtDelegateWidgetAccessible::isValid() const
{
    if (!viewAccessible() || !viewAccessible()->isValid())
        return false;

    return QAccessibleWidget::isValid();
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginewidgets/qwebengine_accessible.cpp, line 78, as _ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible10focusChildEv
namespace QtWebEngineCore {
inline QAccessibleInterface *RenderWidgetHostViewQtDelegateWidgetAccessible::focusChild() const
{
    return viewAccessible()->focusChild();
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginewidgets/qwebengine_accessible.cpp, line 83, as _ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible10childCountEv
namespace QtWebEngineCore {
inline int RenderWidgetHostViewQtDelegateWidgetAccessible::childCount() const
{
    return viewAccessible()->childCount();
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginewidgets/qwebengine_accessible.cpp, line 88, as _ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible5childEi
namespace QtWebEngineCore {
inline QAccessibleInterface *RenderWidgetHostViewQtDelegateWidgetAccessible::child(int index) const
{
    return viewAccessible()->child(index);
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginewidgets/qwebengine_accessible.cpp, line 93, as _ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible12indexOfChildEPK20QAccessibleInterface
namespace QtWebEngineCore {
inline int RenderWidgetHostViewQtDelegateWidgetAccessible::indexOfChild(const QAccessibleInterface *c) const
{
    return viewAccessible()->indexOfChild(c);
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginewidgets/qwebengine_accessible.cpp, line 64, as _ZN15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessibleC1EP7QWidgetP14QWebEngineView
namespace QtWebEngineCore {
inline RenderWidgetHostViewQtDelegateWidgetAccessible::RenderWidgetHostViewQtDelegateWidgetAccessible(QWidget *o, QWebEngineView *view)
    : QAccessibleWidget(o)
    , m_view(view)
{
}
}  // namespace QtWebEngineCore

//  from ../qtwebengine/src/webenginewidgets/qwebengine_accessible.cpp, line 98, as _ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible14viewAccessibleEv
namespace QtWebEngineCore {
inline QWebEngineViewAccessible *RenderWidgetHostViewQtDelegateWidgetAccessible::viewAccessible() const
{
    return static_cast<QWebEngineViewAccessible *>(QAccessible::queryAccessibleInterface(m_view));
}
}  // namespace QtWebEngineCore
//  -----------------------------------------------------------------------

//  QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::RenderWi
//      dgetHostViewQtDelegateWidgetAccessible(QWidget *o, QWebEngineView
//      *view)
extern "C" Q_DECL_EXPORT
QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible *ritual_ZN15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessibleC1EP7QWidgetP14QWebEngineView(
    QWidget *o,
    QWebEngineView *view) {
  return new QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible(
      o,
      view);
}

//  bool QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::isV
//      alid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible7isValidEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible *self) {
  return self->isValid();
}

//  QAccessibleInterface *QtWebEngineCore::RenderWidgetHostViewQtDelegateWidg
//      etAccessible::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible10focusChildEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible *self) {
  return self->focusChild();
}

//  int QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::chil
//      dCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible10childCountEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible *self) {
  return self->childCount();
}

//  QAccessibleInterface *QtWebEngineCore::RenderWidgetHostViewQtDelegateWidg
//      etAccessible::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible5childEi(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible *self,
    int index) {
  return self->child(index);
}

//  int QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::inde
//      xOfChild(const QAccessibleInterface *child) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible12indexOfChildEPK20QAccessibleInterface(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

//  QWebEngineViewAccessible *QtWebEngineCore::RenderWidgetHostViewQtDelegate
//      WidgetAccessible::viewAccessible() const
extern "C" Q_DECL_EXPORT
QWebEngineViewAccessible *ritual_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible14viewAccessibleEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible *self) {
  return self->viewAccessible();
}

//  bool QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::isV
//      alid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible7isValidEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible *self) {
  return self->QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::isValid();
}

//  QAccessibleInterface *QtWebEngineCore::RenderWidgetHostViewQtDelegateWidg
//      etAccessible::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible10focusChildEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible *self) {
  return self->QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::focusChild();
}

//  int QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::chil
//      dCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible10childCountEv(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible *self) {
  return self->QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::childCount();
}

//  QAccessibleInterface *QtWebEngineCore::RenderWidgetHostViewQtDelegateWidg
//      etAccessible::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible5childEi(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible *self,
    int index) {
  return self->QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::child(
      index);
}

//  int QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::inde
//      xOfChild(const QAccessibleInterface *child) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QtWebEngineCore46RenderWidgetHostViewQtDelegateWidgetAccessible12indexOfChildEPK20QAccessibleInterface(
    const QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible *self,
    const QAccessibleInterface *child) {
  return self->QtWebEngineCore::RenderWidgetHostViewQtDelegateWidgetAccessible::indexOfChild(
      child);
}

#endif  // QT_CONFIG(accessibility)
