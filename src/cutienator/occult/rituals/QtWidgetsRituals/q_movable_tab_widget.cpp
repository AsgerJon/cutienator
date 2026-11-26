//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtabbar_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtabbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpixmap.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qlayoutengine_p.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qabstractitemdelegate.h>
#endif
#include <QtWidgets/qapplication.h>
#include <QtGui/qevent.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qstylepainter.h>
#if QT_CONFIG(tabwidget)
#include <QtWidgets/qtabwidget.h>
#endif
#if QT_CONFIG(tooltip)
#include <QtWidgets/qtooltip.h>
#endif
#if QT_CONFIG(whatsthis)
#include <QtWidgets/qwhatsthis.h>
#endif
#include <QtGui/private/qtextengine_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#ifdef Q_OS_MACOS
#include <QtGui/qpa/qplatformnativeinterface.h>
#endif
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qtabbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qtabbar.cpp, line 68, as _ZN17QMovableTabWidgetC1EP7QWidget
inline QMovableTabWidget::QMovableTabWidget(QWidget *parent)
    : QWidget(parent)
{
}

//  from src/widgets/widgets/qtabbar.cpp, line 73, as _ZN17QMovableTabWidget9setPixmapERK7QPixmap
inline void QMovableTabWidget::setPixmap(const QPixmap &pixmap)
{
    m_pixmap = pixmap;
    update();
}

//  from src/widgets/widgets/qtabbar.cpp, line 79, as _ZN17QMovableTabWidget10paintEventEP11QPaintEvent
inline void QMovableTabWidget::paintEvent(QPaintEvent *e)
{
    Q_UNUSED(e);
    QPainter p(this);
    p.drawPixmap(0, 0, m_pixmap);
}
//  -----------------------------------------------------------------------

//  Only a class built on QMovableTabWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMovableTabWidget : QMovableTabWidget {
  using QMovableTabWidget::paintEvent;
};

//  QMovableTabWidget::QMovableTabWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QMovableTabWidget *ritual_ZN17QMovableTabWidgetC1EP7QWidget(
    QWidget *parent) {
  return new QMovableTabWidget(parent);
}

//  void QMovableTabWidget::setPixmap(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMovableTabWidget9setPixmapERK7QPixmap(
    QMovableTabWidget *self,
    const QPixmap *pixmap) {
  self->setPixmap(*pixmap);
}

//  void QMovableTabWidget::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMovableTabWidget10paintEventEP11QPaintEvent(
    QMovableTabWidget *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  void QMovableTabWidget::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QMovableTabWidget10paintEventEP11QPaintEvent(
    QMovableTabWidget *self,
    QPaintEvent *e) {
  static_cast<OwnQMovableTabWidget *>(self)->OwnQMovableTabWidget::paintEvent(
      e);
}

#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(tabbar)
